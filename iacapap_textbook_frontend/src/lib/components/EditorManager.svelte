<script>
	import Editor from '$lib/components/Editor.svelte';
	import { beforeNavigate, goto, invalidateAll } from '$app/navigation';
	import {
		ExitConfirmationAlert,
		SaveCompleteAlert,
		PublishingCompleteAlert
	} from '$lib/components/modal';
	import DeleteAlert from '$lib/components/modal/DeleteAlert.svelte';
	import Preview from '$lib/components/Preview.svelte';
	import { page } from '$app/stores';
	import UnpublishingCompleteAlert from './modal/UnpublishingCompleteAlert.svelte';

	export let editor;
	export let bookTitleValue;
	export let chapterValue;
	export let handleSaveArticle;
	export let handlePublishing;
	export let isPublishingModalOpen;
	export let isSaveModalOpen;
	export let chapterInputEl;
	export let bookTitleInputEl;
	export let articleId;
	export let scrollPosition;
	export let published = false;
	export let handleUnPublishing;
	export let isUnPublishingModalOpen = false;

	beforeNavigate(({ cancel, to }) => {
		if ($page.url.pathname === to.url.pathname) return;

		if (!isExit && !published) {
			cancel();
			isExitModalOpen = true;
		}
		gotoPathName = to.url.pathname;
	});

	let isExit = false; // 페이지 이동 여부
	let gotoPathName; // 이동할 경로

	// 모달 컨트롤 변수
	let isPreviewOpen = false;
	let isExitModalOpen = false;
	let isDeleteModalOpen = false;

	let previewContent = '';

	const closePreview = () => {
		isPreviewOpen = false;
		document.body.style.overflow = 'auto';
	};

	const exit = () => {
		isExit = true;
		goto(gotoPathName);
	};

	const saveAndExit = async () => {
		const isSubmit = await handleSaveArticle();
		if (isSubmit) {
			isExit = true;
			goto(gotoPathName);
		} else {
			isExitModalOpen = false;
		}
	};

	const onDelete = () => {
		editor.setData('');
		isDeleteModalOpen = false;
		bookTitleValue = '';
		chapterValue = '';
	};

	const onSaveDone = async () => {
		isExit = true;
		isSaveModalOpen = false;
		if (scrollPosition) {
			const hash = `#scroll-${scrollPosition}`; // 해시 생성
			goto(`/admin/write/${articleId}${hash}`, { replaceState: true, invalidateAll: true });
			isExit = false;
		} else {
			goto(`/admin/write/${articleId}`);
		}
	};

	const onPublishingDone = () => {
		isExit = true;
		isPublishingModalOpen = false;
		goto('/admin/publishing-list/list');
	};

	const onUnpublishingDone = () => {
		isUnPublishingModalOpen = false;
		goto('/admin/publishing-list/list');
	};

	const showDeleteModal = () => {
		isDeleteModalOpen = true;
	};

	const showPreviewModal = () => {
		isPreviewOpen = true;
		previewContent = editor.getData();
		document.body.style.overflow = 'hidden';
	};

	// 나가기 취소
	const cancelModal = () => {
		isExitModalOpen = false;
	};
</script>

<svelte:window on:keydown={(e) => e.key === 'Escape' && cancelModal()} />
<div class="editor-wrap">
	<Editor
		bind:editor
		{handleSaveArticle}
		{showDeleteModal}
		{handlePublishing}
		{showPreviewModal}
		bind:bookTitleValue
		bind:chapterValue
		bind:chapterInputEl
		bind:bookTitleInputEl
		{published}
		{handleUnPublishing}
	/>
</div>

<ExitConfirmationAlert isModalOpen={isExitModalOpen} {exit} {saveAndExit} />
<DeleteAlert
	isModalOpen={isDeleteModalOpen}
	onCancel={() => (isDeleteModalOpen = false)}
	{onDelete}
/>
<SaveCompleteAlert isModalOpen={isSaveModalOpen} openPreview={showPreviewModal} {onSaveDone} />
<PublishingCompleteAlert isModalOpen={isPublishingModalOpen} closeModal={onPublishingDone} />
<UnpublishingCompleteAlert isModalOpen={isUnPublishingModalOpen} closeModal={onUnpublishingDone} />
<Preview
	previewOpen={isPreviewOpen}
	content={previewContent}
	{bookTitleValue}
	{chapterValue}
	{closePreview}
/>

<style lang="scss">
	.editor-wrap {
		padding: 0 120px 40px;
		position: relative;
	}
</style>
