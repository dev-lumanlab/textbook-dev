<script>
	import { dateFormat } from '$lib/utils/dateFormat';
	import { Trash2 } from '$lib/components/icons';

	export let id;
	export let book;
	export let title;
	export let chapter;
	export let last_update;
	// export let last_publish;
	export let thumbnail;
	export let published;
	export let onDelete;
	export let onBackup;
	export let onPublishing = () => {};
</script>

<li class="item">
	<a href="/admin/write/{id}">
		<div class="image">
			<img src={thumbnail ? thumbnail : '/no-image.png'} alt="썸네일" />
		</div>
		<div class="content">
			<h3>{@html title}</h3>
			<div class="info-container">
				<p class="chapter">{book} {chapter}</p>
				{#if published}
					<p class="date">Last Publishing {dateFormat(last_update)}</p>
				{:else}
					<p class="date">Last Update {dateFormat(last_update)}</p>
				{/if}
			</div>
		</div>
		<div class="tag">
			<div>
				<!-- {#if published}
					<span class="publishing-date">
						Last Publishing {dateFormat(last_publish)}
					</span>
				{/if} -->
			</div>
			<div class="right">
				{#if published}
					<button class="backup" on:click|preventDefault={() => onBackup(id)}
						>Import to save list</button
					>
				{:else}
					<button class="backup" on:click|preventDefault={() => onPublishing(id)}>Publishing</button
					>
				{/if}
				<button class="delete" on:click|preventDefault={() => onDelete(id)}
					><Trash2 width={12} height={14} /></button
				>
			</div>
		</div>
	</a>
</li>

<style lang="scss">
	.item a {
		border-radius: 8px;
		overflow: hidden;
		background-color: #fff;
		display: flex;
		flex-direction: column;
		box-shadow: 0px 10px 15px -3px #0000000a;
		position: relative;
		height: 100%;

		&:hover {
			img {
				transform: scale(1.05);
				transition-property: transform;
				transition-duration: 0.2s;
			}
		}

		.image {
			background: #eceef0;
			img {
				width: 100%;
				height: 216px;
				object-fit: cover;
				display: block;
			}
		}

		.content {
			flex: 1;
			padding: 20px 20px 28px;
			display: flex;
			flex-direction: column;
			justify-content: space-between;

			h3 {
				font-size: 20px;
				line-height: 30px;
				font-weight: 600;
				margin-bottom: 16px;
			}

			.chapter {
				color: var(--slate-color);
				font-size: 16px;
				line-height: 24px;
				margin-bottom: 2px;
			}

			.date {
				font-size: 16px;
				line-height: 24px;
			}
		}

		.tag {
			position: absolute;
			display: flex;
			justify-content: space-between;
			width: 100%;
			top: 0;
			left: 0;
			padding: 16px;

			// .publishing-date {
			// 	padding: 4px 8px;
			// 	background-color: var(--blue-color);
			// 	font-size: 12px;
			// 	line-height: 18px;
			// 	border-radius: 4px;
			// 	color: white;
			// 	display: block;
			// }

			.right {
				display: flex;
				align-items: center;
				gap: 8px;

				.backup {
					padding: 6px 10px;
					color: var(--slate-color);
					font-weight: 500;
					font-size: 14px;
					line-height: 20px;
					border-radius: 6px;
					background: #fff;
				}
				.delete {
					width: 32px;
					height: 32px;
					border-radius: 6px;
					background-color: #fff;
					display: flex;
					justify-content: center;
					align-items: center;
				}
			}
		}
	}
</style>
