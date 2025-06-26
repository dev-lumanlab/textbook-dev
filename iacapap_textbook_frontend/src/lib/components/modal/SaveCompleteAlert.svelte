<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let openPreview;
	export let onSaveDone;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/check.png">
	<span slot="title">Saving is complete..</span>
	<span slot="content">Please click the publishing button to upload the completed textbook.</span>
	<div class="btn-wrap" slot="buttons">
		<button class="btn type2 out" on:click={openPreview}>Preview</button>
		<button class="btn type1 save" on:click={onSaveDone}>Done</button>
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
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
