<script>
	import { Close } from '$lib/components/icons';
	import '$styles/editor.scss';
	export let previewOpen = false;
	export let content;
	export let bookTitleValue = '';
	export let chapterValue = '';
	export let closePreview;
</script>

{#if previewOpen}
	<div class="overlay">
		<div class="header">
			<div class="wrap">
				<span>Preview</span>
				<button on:click={closePreview}><Close /></button>
			</div>
		</div>
		<div class="container">
			<div class="wrap">
				<div class="chapter">
					<h2>{bookTitleValue}</h2>
					<span>Chapter {chapterValue}</span>
				</div>
				<div id="editor" class="contents">
					{@html content}
				</div>
			</div>
		</div>
	</div>
{/if}

<style lang="scss">
	.overlay {
		background: #fff;
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: 99999;
	}

	.wrap {
		padding: 24px;
	}

	.header {
		border-bottom: 1px solid #d7dbdf;

		.wrap {
			display: flex;
			justify-content: space-between;
			align-items: center;

			span {
				font-size: 24px;
			}

			button {
				width: 20px;
				height: 20px;
				display: flex;
				justify-content: center;
				align-items: center;
			}
		}
	}

	.container {
		height: 100%;
		overflow: auto;
		padding-bottom: 24px;
		.chapter {
			display: flex;
			align-items: center;
			justify-content: space-between;
			background: var(--blue-color);
			padding: 42px 24px 42px 72px;
			border-radius: 16px;
			color: #fff;
			position: relative;

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
		.contents {
			padding: 0 48px 0;
		}
	}
</style>
