<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let closeModal;
</script>

<AlertModal isOpen={isModalOpen} bgImage="/AssetonShape.png">
	<span slot="title">구글 로그인 사용자가 아닙니다.</span>
	<span slot="content">
		입력하신 정보를 <br />
		다시 확인해주세요.
	</span>
	<button slot="buttons" class="btn type1" on:click={closeModal}>확인</button>
</AlertModal>

<style lang="scss">
	.btn.type1 {
		font-size: 14px;
		line-height: 20px;
		padding: 10px;
	}
</style>
