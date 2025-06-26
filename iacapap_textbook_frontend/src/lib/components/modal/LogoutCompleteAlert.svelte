<script>
	import Modal from './Modal.svelte';

	export let isModalOpen = false;
	export let closeModal;
	export let onLogoutDone;
</script>

<Modal isOpen={isModalOpen}>
	<div class="modal-wrap">
		<h2 class="modal-title">Do you want to log out?</h2>
		<p>You can log in again at any time.</p>
		<div class="btn-wrap">
			<button class="btn type2" on:click={closeModal}>Cancel</button>
			<button class="btn type1" on:click={onLogoutDone}>Logout</button>
		</div>
	</div>
</Modal>

<style lang="scss">
	.modal-wrap {
		width: 336px;

		h2 {
			font-size: 20px;
			line-height: 30px;
			font-weight: 600;
			margin-bottom: 12px;
			padding: 3px 0;
		}
		p {
			font-size: 16px;
			line-height: 26px;
			margin-bottom: 22px;
		}
		.btn-wrap {
			display: flex;
			justify-content: space-between;
			align-items: center;
			width: 100%;
			gap: 8px;

			.btn {
				width: auto;
			}

			button {
				flex: 1;
			}
		}

		.btn.type1 {
			font-size: 14px;
			line-height: 20px;
			padding: 10px;
		}
	}
</style>
