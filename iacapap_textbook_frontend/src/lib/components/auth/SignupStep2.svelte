<script>
	import { EmailInput } from '$lib/components/input';

	export let email;
	export let onSubmit;
</script>

<div>
	<div class="img-wrap">
		<div class="img"></div>
	</div>
	<div>
		<EmailInput label="Enter your email." value={email} disabled={true} />
	</div>
	<p>
		Check your inbox for confirmation messages. If you haven't received them, check your spammybox
		or <button on:click={onSubmit}>email them again.</button>
	</p>
</div>

<style lang="scss">
	.img-wrap {
		display: flex;
		justify-content: center;
		margin-bottom: 46px;

		.img {
			width: 246px;
			height: 139px;
			background: url('/signup.png') no-repeat center center;
		}
	}
	p {
		text-align: left;
		font-size: 16px;
		line-height: 24px;
		margin-top: 24px;

		button {
			font-size: inherit;
			line-height: inherit;
			font-weight: inherit;
			color: var(--blue-color);
		}
	}
</style>
