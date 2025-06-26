<script>
	import Trash from '$lib/components/icons/Trash.svelte';
	import { dateTimeFormat } from '$lib/utils/dateFormat';
	import { highlightStore } from '../../../stores/highlight';
	import DeleteHighlightAlert from '../modal/DeleteHighlightAlert.svelte';
	import Sidebar from './Sidebar.svelte';

	export let show = false;

	let highlightId = null;
	let isShow = false;

	const closeDeleteModal = () => {
		isShow = false;
		highlightId = null;
	};

	const onDeleteDone = () => {
		isShow = false;
		highlightStore.remove(highlightId);
		highlightId = null;
	};

	const onDelete = (id) => {
		isShow = true;
		highlightId = id;
	};
</script>

<Sidebar bind:show title="Highlight">
	<div class="content">
		<ul>
			{#each $highlightStore as { text, created_at, id }}
				<li>
					<p>{text}</p>
					<div class="bottom">
						<div>
							<span class="date">{dateTimeFormat(created_at)}</span>
						</div>
						<button on:click={() => onDelete(id)}><Trash /></button>
					</div>
				</li>
			{/each}
		</ul>
	</div>
</Sidebar>

<DeleteHighlightAlert isModalOpen={isShow} closeModal={closeDeleteModal} {onDeleteDone} />

<style lang="scss">
	.content {
		padding: 0 32px 32px;

		ul {
			display: flex;
			flex-direction: column;
			gap: 32px;
		}

		li {
			border-radius: 16px;
			border: 1px solid var(--slate-base-color);
			padding: 23px 23px 0;

			p {
				font-size: 24px;
				line-height: 42px;
				margin-bottom: 23px;
			}

			.bottom {
				display: flex;
				justify-content: space-between;
				align-items: center;
				padding: 10px 0;

				.date {
					font-size: 14px;
					line-height: 24px;
					color: var(--slate-base-color);
				}

				button {
					width: 32px;
					height: 32px;
					display: flex;
					align-items: center;
					justify-content: center;
				}
			}
		}
	}
</style>
