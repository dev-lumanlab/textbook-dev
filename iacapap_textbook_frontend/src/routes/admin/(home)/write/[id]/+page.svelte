<script>
	import { page } from '$app/stores';
	import {
		getSaveArticle,
		patchSaveArticle,
		postPublishingArticle,
		postUnPublishingArticle
	} from '$lib/api/docs';
	import EditorManager from '$lib/components/EditorManager.svelte';
	import { addUUIDToHeadings } from '$lib/utils/editor.js';
	import { onMount, tick } from 'svelte';

	export let data;

	let chapterInputEl;
	let bookTitleInputEl;
	let bookTitleValue = '';
	let chapterValue = '';
	let editor = null;
	let isPublishingModalOpen = false;
	let isSaveModalOpen = false;
	let isUnPublishingModalOpen = false;

	let published;

	let scrollPosition = 0;

	$: articleId = $page.params.id;

	onMount(async () => {
		const article = data.article;
		bookTitleValue = article.book;
		chapterValue = article.chapter.replace('Chapter ', '');
		published = article.published;
	});

	$: if (editor && data) {
		editor.setData(data.article.content);

		tick().then(() => {
			const hash = window.location.hash;
			if (hash) {
				const scrollPosition = parseInt(hash.replace('#scroll-', ''), 10);
				window.scrollTo(0, scrollPosition);
			}
		});
	}

	const validateData = () => {
		const isBookTitleValid = bookTitleValue !== '';
		const isChapterValid = chapterValue !== '';
		const isTitleValid = editor.plugins.get('Title').getTitle() !== '';

		if (!isBookTitleValid) {
			bookTitleInputEl.focus();
			return false;
		}

		if (!isChapterValid) {
			chapterInputEl.focus();
			return false;
		}

		if (!isTitleValid) {
			editor.focus();
			return false;
		}

		return true;
	};

	const handleSubmit = async (action) => {
		const title = editor.plugins.get('Title').getTitle();
		const content = addUUIDToHeadings(editor.getData());
		const chapter = `Chapter ${chapterValue}`;
		const book = bookTitleValue;
		const isValid = validateData();

		if (!isValid) return;

		const data = { book, title, content, chapter };

		try {
			await patchSaveArticle(articleId, data);

			if (action === 'publish') {
				await postPublishingArticle(articleId);
				isPublishingModalOpen = true;
			} else {
				scrollPosition = window.scrollY;
				isSaveModalOpen = true;
			}

			return true;
		} catch (error) {
			console.error(error);
		}
	};

	const handleUnPublishing = async () => {
		try {
			await postUnPublishingArticle(articleId);
			isUnPublishingModalOpen = true;
		} catch (error) {
			console.error(error);
		}
	};

	const handlePublishing = () => handleSubmit('publish');
	const handleSaveArticle = () => handleSubmit('save');
</script>

<svelte:head>
	<title>'{data.article.book}' Modify - IACAPAP</title>
</svelte:head>

<EditorManager
	bind:editor
	bind:isPublishingModalOpen
	bind:isSaveModalOpen
	{handlePublishing}
	{handleSaveArticle}
	{articleId}
	{scrollPosition}
	bind:bookTitleValue
	bind:chapterValue
	bind:chapterInputEl
	bind:bookTitleInputEl
	bind:isUnPublishingModalOpen
	{published}
	{handleUnPublishing}
/>
