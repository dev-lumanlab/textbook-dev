<script>
	import { highlightStore } from '$stores/highlight';
	import HighlightPopup from '$lib/components/HighlightPopup.svelte';
	import mark from 'mark.js/dist/mark';
	import { onMount } from 'svelte';
	import {
		calculateRelativeOffsets,
		findBlockIndex,
		getBlocks,
		getSelectedTextInfo
	} from '$lib/utils/highlight';
	import rehypeSlug from 'rehype-slug';
	import { rehype } from 'rehype';

	export let data;
	export let articleId;
	let contentBlocks = null;

	let rehypeContent; // heading 태그에 id 추가하기 위한 변수
	let textContainer;
	let selectionRect = null;
	let isShowPopup = false;

	let textInfo = null;
	let submitData = null;
	let markInstance;

	onMount(async () => {
		rehypeContent = data.content.content;

		await rehype()
			.data('settings', { fragment: true })
			.use(rehypeSlug)
			.process(rehypeContent)
			.then((file) => {
				rehypeContent = String(file);
			});
		contentBlocks = getBlocks(textContainer);
	});

	$: if (contentBlocks) {
		const options = {
			acrossElements: true,
			separateWordSearch: false,
			accuracy: 'exactly',
			element: 'mark',
			className: 'highlight'
		};

		if (markInstance) {
			markInstance.unmark(options);
		}

		if ($highlightStore.length > 0) {
			$highlightStore.forEach((item) => {
				markInstance = new mark(contentBlocks[item.block]);
				markInstance.markRanges([{ start: item.start, length: item.end - item.start }], options);
			});
		}
	}

	const handleMouseUp = () => {
		const textCalculateRelativeOffsets = calculateRelativeOffsets();

		const blockIndex = findBlockIndex(textContainer);

		textInfo = getSelectedTextInfo();

		if (blockIndex) {
			submitData = {
				block: blockIndex,
				...textCalculateRelativeOffsets,
				text: textInfo
			};
		}
	};

	const handleMouseDown = (e) => {
		if (e.button !== 2) {
			selectionRect = null;
			submitData = null;
			isShowPopup = false;
		}
	};

	const handleContextMenu = (e) => {
		selectionRect = { x: e.pageX, y: e.pageY };

		if (selectionRect && submitData) {
			isShowPopup = true;
		} else {
			isShowPopup = false;
		}
	};

	const onSubmit = async () => {
		highlightStore.post(articleId, submitData);
		isShowPopup = false;
	};
</script>

<div class="title">
	<h2>{data.content.book}</h2>
	<span>{data.content.chapter}</span>
</div>

<div
	id="editor"
	class="content"
	on:mouseup={handleMouseUp}
	on:contextmenu|preventDefault={handleContextMenu}
	on:mousedown={handleMouseDown}
	role="button"
	tabindex="0"
	bind:this={textContainer}
>
	{@html rehypeContent}
</div>

<HighlightPopup position={selectionRect} {textInfo} {onSubmit} bind:isShow={isShowPopup} />

<style lang="scss">
	.title {
		display: flex;
		align-items: center;
		justify-content: space-between;
		background: var(--blue-color);
		padding: 42px 24px 42px 72px;
		border-radius: 16px;
		color: #fff;

		h2 {
			font-weight: 900;
			font-size: 48px;
			line-height: 60px;
		}

		span {
			font-size: 32px;
			line-height: 40px;
			padding: 22px 46px;
			border-radius: 99px;
			font-weight: 500;
			border: 2px solid #fff;
		}
	}

	.content {
		position: relative;
		padding: 40px 48px 0;
	}
</style>
