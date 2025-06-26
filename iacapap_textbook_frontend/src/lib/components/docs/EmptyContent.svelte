<script>
	export let description = 'No content';
</script>

<div class="container">
	<div class="no-contents"></div>
	<p>{description}</p>
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 82px 0;
		background: #fff;
		border-radius: 16px;
	}

	.no-contents {
		background-image: url('/no-contents.png');
		background-size: contain;
		background-repeat: no-repeat;
		width: 304px;
		height: 125px;
		margin-bottom: 32px;
	}

	p {
		font-size: 16px;
		line-height: 26px;
		margin-bottom: 8px;
	}
</style>
