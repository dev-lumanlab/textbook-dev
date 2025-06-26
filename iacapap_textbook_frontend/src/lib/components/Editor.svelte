<script>
	import { onMount, tick } from 'svelte';
	import '$styles/editor.scss';
	import { Trash2 } from '$lib/components/icons/Trash2';
	import { uploadFile } from '$lib/api/editor/upload';

	export let editor;
	export let showDeleteModal;
	export let showPreviewModal;
	export let handleSaveArticle;
	export let handlePublishing;
	export let bookTitleValue;
	export let chapterValue;
	export let chapterInputEl;
	export let bookTitleInputEl;
	export let published;
	export let handleUnPublishing;

	let toolbarTopPosition = 0;
	let chapterEl;
	let editorEditableEl;

	$: chapterVisible = editor ? 'visible' : 'hidden';

	onMount(async () => {
		await import('https://tistory1.daumcdn.net/tistory/7059211/skin/images/ckeditor.js');

		ClassicEditor.create(document.querySelector('#editor'))
			.then(async (newEditor) => {
				editor = newEditor;

				editorEditableEl = document.querySelector('.ck-editor__editable');

				uploadFile(editor);

				const toolbar = editor.ui.view.toolbar.element;
				toolbarTopPosition = toolbar.offsetTop + toolbar.offsetHeight + 1; // 1px 추가한건 border 값 때문

				const editorBody = document.querySelector('.ck-editor__main');
				editorBody.style.marginTop = `${chapterEl.offsetHeight}px`;

				await tick();
				bookTitleInputEl.focus();
			})
			.catch((error) => {
				console.error(error);
			});
	});

	// 툴바 커스텀 버튼
	$: if (editor) {
		const editorToolbar = document.querySelector('.ck.ck-toolbar');
		const btnWrap = document.createElement('div');
		btnWrap.className = 'btn-wrap';

		if (published) {
			editor.enableReadOnlyMode('editor');
			const publishingButton = document.createElement('button');
			publishingButton.className = 'Unpublishing';
			publishingButton.innerText = 'Unpublishing';
			publishingButton.addEventListener('click', handleUnPublishing);
			btnWrap.appendChild(publishingButton);
		} else {
			const trashButton = document.createElement('button');
			trashButton.className = 'trash';
			trashButton.innerHTML = Trash2();
			trashButton.addEventListener('click', showDeleteModal);

			const submitButton = document.createElement('button');
			submitButton.innerText = 'Save';
			submitButton.addEventListener('click', handleSaveArticle);

			const previewButton = document.createElement('button');
			previewButton.innerText = 'Preview';
			previewButton.addEventListener('click', showPreviewModal);

			const publishingButton = document.createElement('button');
			publishingButton.className = 'publishing';
			publishingButton.innerText = 'Publishing';
			publishingButton.addEventListener('click', handlePublishing);

			btnWrap.appendChild(trashButton);
			btnWrap.appendChild(submitButton);
			btnWrap.appendChild(previewButton);
			btnWrap.appendChild(publishingButton);
		}
		editorToolbar.appendChild(btnWrap);
	}

	// tabindex 접근성
	const handleChapterValueKeyDown = (event) => {
		if (event.key === 'Tab') {
			editorEditableEl.focus();
			event.preventDefault();
		}
	};
</script>

<div class="wrap">
	<div id="editor"></div>

	<div
		class="editor-chapter"
		style="top: {toolbarTopPosition}px; visibility: {chapterVisible}"
		bind:this={chapterEl}
	>
		<div class="chapter-wrap">
			<input
				type="text"
				class="chapter-title"
				placeholder="book Title"
				bind:value={bookTitleValue}
				bind:this={bookTitleInputEl}
				disabled={published}
			/>
			<div class="chapter-version-wrap">
				<span>Chapter</span>
				<input
					type="text"
					class="chapter-version"
					bind:value={chapterValue}
					bind:this={chapterInputEl}
					on:keydown={handleChapterValueKeyDown}
					disabled={published}
				/>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.wrap {
		position: relative;

		.editor-chapter {
			position: absolute;
			width: 100%;
			padding: 24px;
			z-index: 10;
			background-color: #fff;

			.chapter-wrap {
				padding: 24px;
				background: #308fff;
				border-radius: 16px;
				display: flex;
				justify-content: space-between;
				align-items: center;

				.chapter-title {
					background: transparent;
					border: none;
					font-size: 48px;
					color: white;
					line-height: 60px;
					width: 800px;
				}

				.chapter-version-wrap {
					padding: 23px 47px;
					border-radius: 99px;
					border: 2px solid #fff;
					color: #fff;
					font-size: 32px;
					line-height: 40px;
					display: flex;
					align-items: center;
					gap: 10px;

					input {
						background: transparent;
						border: none;
						font-size: 32px;
						line-height: 40px;
						color: #fff;
						width: 60px;
					}
				}
			}
		}
	}
</style>
