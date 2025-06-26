<script>
	import AdminDocsItem from './AdminDocsItem.svelte';

	export let contents = [];
	export let onDelete;
	export let onBackup = () => {};
	export let onPublishing = () => {};
</script>

<div class="contents">
	<ul class="list">
		{#if contents.length > 0}
			{#each contents as { id, title, book, chapter, last_update, last_publish, published }}
				<AdminDocsItem
					{onDelete}
					{onPublishing}
					{id}
					{book}
					{title}
					{chapter}
					{last_update}
					{last_publish}
					{published}
					{onBackup}
				/>
			{/each}
		{/if}
	</ul>
</div>

<style lang="scss">
	.contents {
		.list {
			display: flex;
			flex-direction: column;
			border-radius: 16px;
			gap: 8px;
			box-shadow: 0px 10px 15px -3px #00000014;
			// box-shadow: 0px 4px 6px -2px #00000005;
		}
	}
</style>
