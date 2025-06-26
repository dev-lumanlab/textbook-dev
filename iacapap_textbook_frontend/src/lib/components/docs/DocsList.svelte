<script>
	import DocsItem from './DocsItem.svelte';

	export let contents = [];
	export let alignItemsCenter = false;
	export let includeSeconds = false;
	export let observeTarget;
</script>

<div class="contents">
	<ul>
		{#each contents as { id, title, chapter, book, last_update }}
			<DocsItem
				{id}
				{title}
				{book}
				{chapter}
				date={last_update}
				{alignItemsCenter}
				{includeSeconds}
			/>
		{/each}
		<li bind:this={observeTarget}></li>
	</ul>
</div>

<style lang="scss">
	.contents {
		display: flex;
		flex-direction: column;
		max-height: 765px;
		background-color: #fff;
		border-radius: 16px;
		overflow: hidden;

		box-shadow: 0px 10px 15px -3px #00000014;

		ul {
			display: flex;
			padding-left: 20px;
			padding-right: 24px;
			flex-direction: column;
			gap: 8px;
			overflow: auto;

			margin-bottom: 4px;
			margin-right: 4px;
			margin-top: 4px;
		}
	}
</style>
