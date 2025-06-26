<main>
	<div>
		<h1><img src="/logo.png" alt="로고" /></h1>
		<div class="container">
			<slot />
		</div>
		<div class="bottom-logo">
			<img src="/logo2.png" alt="로고" />
		</div>
	</div>
</main>

<style lang="scss">
	main {
		text-align: center;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100%;
	}

	h1 {
		margin-bottom: 24px;

		img {
			width: 203px;
		}
	}

	.container {
		display: flex;
		flex-direction: column;
		gap: 24px;
		background: #fff;
		border-radius: 16px;
		padding: 48px;
		width: 432px;
	}

	.bottom-logo img {
		width: 291.87px;
		height: 40px;
		margin-top: 24px;
	}
</style>
