<script>
	import AlertModal from './AlertModal.svelte';

	export let isModalOpen = false;
	export let closeModal;

	/**
	 * @type {"ko" | "en"}
	 */
	export let lang = 'ko';
</script>

<AlertModal isOpen={isModalOpen} bgImage="/AssetonShape.png">
	<span slot="title">
		{#if lang === 'ko'}
			로그인 실패
		{:else}
			Login Failed
		{/if}
	</span>
	<span slot="content">
		{#if lang === 'ko'}
			이메일 또는 비밀번호가 일치하지 않습니다.<br />입력한 정보를 다시 확인해 주세요.
		{:else}
			Your email or password does not match.<br />Please check the information<br />you entered
			again.
		{/if}
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
