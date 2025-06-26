<script>
	import { postPublishingArticle, postSaveArticle } from '$lib/api/docs';
	import EditorManager from '$lib/components/EditorManager.svelte';
	import { addUUIDToHeadings } from '$lib/utils/editor';

	let chapterInputEl;
	let bookTitleInputEl;
	let bookTitleValue = '';
	let chapterValue = '';
	let editor = null;
	let isPublishingModalOpen = false;
	let isSaveModalOpen = false;
	let articleId = null;

	let scrollPosition = 0;

	const validateData = () => {
		const isBookTitleValid = bookTitleValue.trim() !== '';
		const isChapterValid = chapterValue.trim() !== '';
		const isTitleValid = editor.plugins.get('Title').getTitle().trim() !== '';

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
			const response = await postSaveArticle(data);
			articleId = response.data.content.article_id;

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

	const handlePublishing = () => handleSubmit('publish');
	const handleSaveArticle = () => handleSubmit('save');
</script>

<svelte:head>
	<title>Write - IACAPAP</title>
</svelte:head>

<EditorManager
	bind:editor
	bind:isSaveModalOpen
	bind:isPublishingModalOpen
	{handlePublishing}
	{handleSaveArticle}
	{articleId}
	{scrollPosition}
	bind:bookTitleValue
	bind:chapterValue
	bind:chapterInputEl
	bind:bookTitleInputEl
/>
