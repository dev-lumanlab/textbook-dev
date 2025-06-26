<script>
	import { EmailInput } from '$lib/components/input';
	import { isValidEmail } from '$lib/utils/emailValidator';

	export let email = '';
	export let onSubmit;

	let disabled = true;

	$: disabled = isValidEmail(email) === false;
</script>

<h2>
	Did you forget your<br /> password?
	<span>Please enter the email you joined.</span>
</h2>

<div class="form-input">
	<form on:submit|preventDefault={onSubmit}>
		<div class="input-wrap">
			<EmailInput label="Email" bind:value={email} />
		</div>
		<div class="btn-wrap">
			<button class="btn type1" class:disabled {disabled}>Email Authentication</button>
		</div>
	</form>
</div>

<style lang="scss">
	h2 {
		font-size: 26px;
		line-height: 36px;
		font-weight: 500;

		span {
			display: block;
			font-size: 16px;
			line-height: 24px;
			color: var(--slate-base-color);
		}
	}

	.form-input {
		.input-wrap {
			margin-bottom: 24px;
		}
	}
</style>
