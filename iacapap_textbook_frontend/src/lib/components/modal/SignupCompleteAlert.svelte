<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let closeModal;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/check2.png">
	<span slot="title">회원가입 완료!</span>
	<span slot="content">지금 바로 다양한 콘텐츠를 무제한으로 확인하세요.</span>
	<button slot="buttons" class="btn type1" on:click={closeModal}>확인</button>
</AlertModal>

<style lang="scss">
	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
