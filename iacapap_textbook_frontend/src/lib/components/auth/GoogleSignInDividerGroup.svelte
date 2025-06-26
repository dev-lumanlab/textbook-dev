<script>
	import { page } from '$app/stores';
	import { PUBLIC_GOOGLE_CLIENT_ID } from '$env/static/public';
	import { onMount } from 'svelte';

	export let isSignup = true;

	let GOOGLE_LOGIN_URI;

	onMount(() => {
		const GOOGLE_REDIRECT_URL = isSignup
			? `${$page.url.origin}/auth/google/signup`
			: `${$page.url.origin}/auth/google/signin`;
		GOOGLE_LOGIN_URI = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${PUBLIC_GOOGLE_CLIENT_ID}&redirect_uri=${GOOGLE_REDIRECT_URL}&response_type=code&scope=email profile`;
	});
</script>

<div class="divider">
	<div class="line"></div>
	<span>or</span>
	<div class="line"></div>
</div>

<div class="google-login">
	<a href={GOOGLE_LOGIN_URI}>
		<img src="/google.png" alt="구글 로고" />
		<span>Continue with Google</span>
	</a>
</div>

<style lang="scss">
	.divider {
		font-size: 14px;
		line-height: 20px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 12px;

		span {
			color: #687076;
		}

		.line {
			width: 100%;
			height: 1px;
			background: #dfe3e6;
		}
	}

	.google-login a {
		display: flex;
		justify-content: center;
		align-items: center;
		gap: 10px;
		border-radius: 6px;
		border: 1px solid #d7dbdf;
		padding: 12px 16px;

		img {
			width: 22px;
			height: 22px;
		}
	}
</style>
