<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let closeModal;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/check2.png">
	<span slot="title">Your password has been<br />changed.</span>
	<span slot="content">
		Press the login button below<br />Please log in with the changed password.</span
	>
	<button slot="buttons" class="btn type1" on:click={closeModal}>로그인</button>
</AlertModal>

<style lang="scss">
	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
