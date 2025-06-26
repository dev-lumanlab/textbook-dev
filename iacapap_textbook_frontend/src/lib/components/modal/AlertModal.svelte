<script>
	import Modal from './Modal.svelte';

	export let isOpen = false;
	export let bgImage = '';
</script>

<Modal {isOpen}>
	<div class="modal-wrap">
		<div style="background-image: url('{bgImage}')" class="image-container"></div>
		<h2 class="modal-title">
			<slot name="title" />
		</h2>
		<p class="modal-content">
			<slot name="content" />
		</p>
		<slot name="buttons" />
	</div>
</Modal>

<style lang="scss">
	.modal-wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 256px;

		.image-container {
			width: 48px;
			height: 48px;
			background-size: contain; /* 이미지가 요소에 맞게 확대/축소되도록 설정 */
			background-position: center; /* 이미지가 가운데에 위치하도록 설정 */
			margin-bottom: 12px;
		}

		.modal-title {
			font-size: 20px;
			line-height: 30px;
			font-weight: 600;
			margin-bottom: 4px;
			text-align: center;
		}

		.modal-content {
			font-size: 14px;
			line-height: 20px;
			color: #687076;
			margin-bottom: 16px;
			text-align: center;
		}
	}
</style>
