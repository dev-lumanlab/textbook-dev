<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let closeModal;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/check.png">
	<span slot="title">Publishing complete</span>
	<span slot="content">
		The contents of the textbook you created have been uploaded to the web normally.
	</span>
	<button slot="buttons" class="btn type1" on:click={closeModal}>Done</button>
</AlertModal>

<style lang="scss">
	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
