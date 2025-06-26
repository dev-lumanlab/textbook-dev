<script>
	import { onMount } from 'svelte';
	import '$styles/graphics.scss';

	export let data;

	let images = [];

	onMount(() => {
		const parser = new DOMParser();
		const doc = parser.parseFromString(data.content.content, 'text/html');

		const figures = doc.querySelectorAll('img:not(table img), table');

		images = Array.from(figures);
	});
</script>

<div class="wrap">
	<div class="title">
		<h2>Image</h2>
		<span class="line"></span>
	</div>

	<div id="editor">
		<div class="list">
			{#if images.length > 0}
				{#each images as image, i}
					<div class="item">
						{@html image.outerHTML}
					</div>
				{/each}
			{/if}
		</div>
	</div>
</div>

<style lang="scss">
	.wrap {
		padding: 24px 48px;
	}
	.title {
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 12px;
		margin-bottom: 24px;

		h2 {
			font-size: 24px;
			font-weight: 500;
			line-height: 30px;
			color: var(--slate-color);
		}

		.line {
			height: 1px;
			width: 100%;
			background-color: #dfe3e6;
		}
	}

	.item {
		margin-bottom: 80px;
		text-align: center;
	}
</style>
