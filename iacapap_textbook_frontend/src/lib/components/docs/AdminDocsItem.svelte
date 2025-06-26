<script>
	import { dateFormat } from '$lib/utils/dateFormat';
	import { Trash2 } from '$lib/components/icons';

	export let id;
	export let title;
	export let book;
	export let chapter;
	export let last_update;
	export let last_publish;
	export let published;
	export let onDelete;
	export let onBackup;
	export let onPublishing = () => {};
</script>

<li class="item">
	<div class="image"></div>
	<div class="content">
		<a href="/admin/write/{id}">
			<h3>{@html title}</h3>
		</a>
		<ul>
			<li class="chapter">{book} {chapter}</li>
			{#if !published}
				<li class="update-date">Last Update {dateFormat(last_update)}</li>
			{/if}
			{#if published}
				<li class="publishing-date">Last Publishing {dateFormat(last_publish)}</li>
			{/if}
		</ul>
	</div>
	<div class="right">
		{#if published}
			<button class="backup" on:click={() => onBackup(id)}>Import to save list</button>
		{:else}
			<button class="backup" on:click={() => onPublishing(id)}>Publishing</button>
		{/if}

		<button class="delete" on:click|preventDefault={() => onDelete(id)}><Trash2 /></button>
	</div>
</li>

<style lang="scss">
	.item {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 20px;
		gap: 12px;
		background: #fff;
		border-radius: 16px;

		a {
			display: inline-block;

			&:hover {
				text-decoration: underline;
			}
		}

		.image {
			width: 28px;
			height: 28px;
			background-image: url('/page.png');
			background-size: contain;
			background-repeat: no-repeat;
		}

		.content {
			flex: 1;

			h3 {
				font-size: 20px;
				line-height: 30px;
			}

			ul {
				color: var(--slate-base-color);
				font-size: 16px;
				line-height: 24px;
				display: flex;
				gap: 33px;

				li {
					position: relative;

					& + li::before {
						content: '';
						position: absolute;
						left: -16px;
						top: 0;
						bottom: 0;
						margin: auto;
						width: 1px;
						height: 16px;
						background-color: #dfe3e6;
					}
				}
			}
		}

		.right {
			display: flex;
			align-items: center;
			gap: 12px;
			.backup {
				padding: 3px 11px;
				color: var(--slate-color);
				font-weight: 500;
				font-size: 14px;
				line-height: 20px;
				border-radius: 6px;
				background: #fff;
				border: 1px solid #d7dbdf;
				border-radius: 99px;
			}
			.delete {
				width: 28px;
				height: 28px;
				display: flex;
				justify-content: center;
				align-items: center;
			}
		}
	}
</style>
