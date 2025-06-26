<script>
	import { GoogleSignInDividerGroup } from '$lib/components/auth';
	import { EmailInput } from '$lib/components/input';
	import { isValidEmail } from '$lib/utils/emailValidator';

	let disabled = true;

	export let email;
	export let onSubmit;

	$: disabled = isValidEmail(email) === false;
</script>

<h2>Email Authentication</h2>

<div class="form-input">
	<form on:submit|preventDefault={onSubmit}>
		<div class="input-wrap">
			<EmailInput label="Enter your email" bind:value={email} />
		</div>
		<div class="btn-wrap">
			<button class="btn type1" class:disabled {disabled}>To authenticate your email</button>
		</div>
	</form>
</div>

<GoogleSignInDividerGroup />

<style lang="scss">
	h2 {
		font-size: 26px;
		line-height: 36px;
		font-weight: 500;
	}

	.form-input {
		.input-wrap {
			margin-bottom: 24px;
		}
	}
</style>
