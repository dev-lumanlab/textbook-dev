<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let onCancel;
	export let onDelete;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/delete.png">
	<span slot="title">Delete</span>
	<span slot="content">Do you want me to delete the document?</span>
	<div class="btn-wrap" slot="buttons">
		<button class="btn type2 out" on:click={onCancel}>Cancel</button>
		<button class="btn type1 save" on:click={onDelete}>Delete</button>
	</div>
</AlertModal>

<style lang="scss">
	.btn-wrap {
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		gap: 12px;

		.btn {
			width: auto;
		}

		.save {
			flex: 1;
		}
	}

	.btn.type1 {
		background: #f65555;
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
