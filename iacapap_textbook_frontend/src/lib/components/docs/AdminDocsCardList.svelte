<script>
	import AdminDocsCardItem from './AdminDocsCardItem.svelte';

	export let contents = [];
	export let onDelete;
	export let onBackup = () => {};
	export let onPublishing = () => {};
</script>

<div class="contents">
	<ul class="list">
		{#if contents.length > 0}
			{#each contents as { id, title, chapter, book, last_update, last_publish, thumbnail, published }}
				<AdminDocsCardItem
					{onDelete}
					{id}
					{book}
					{title}
					{chapter}
					{thumbnail}
					{last_update}
					{last_publish}
					{published}
					{onBackup}
					{onPublishing}
				/>
			{/each}
		{/if}
	</ul>
</div>

<style lang="scss">
	.contents {
		.list {
			display: grid;
			// grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
			grid-template-columns: repeat(3, 384px);
			grid-auto-rows: 420px;
			gap: 24px;
		}
	}
</style>
