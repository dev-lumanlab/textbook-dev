<script>
	import { GoogleSignInDividerGroup } from '$lib/components/auth';
	import { PasswordInput, EmailInput } from '$lib/components/input';
	import { isValidEmail } from '$lib/utils/emailValidator';

	/**
	 * @type {"admin" | "user"}
	 */
	export let role = 'user';
	export let title = '';
	export let info = '';
	export let email = '';
	export let password = '';
	export let onSubmit;
	export let isSignup = false;

	let disabled = true;

	$: disabled = !(isValidEmail(email) && password.length > 6);
</script>

<div class="admin-content">
	<h2 class:admin={role === 'admin'}>{title}</h2>
	<p class:admin={role === 'admin'}>{info}</p>
</div>

<div class="form-input">
	<form on:submit|preventDefault={onSubmit}>
		<div class="input-wrap">
			<EmailInput label="Email" bind:value={email} />
		</div>
		<div class="input-wrap">
			<PasswordInput label="Password" bind:value={password} />
		</div>
		<div class="btn-wrap">
			<button type="submit" class="btn type1" class:disabled {disabled}>Login</button>
		</div>
	</form>
</div>

<GoogleSignInDividerGroup {isSignup} />

<div class="bottom-frame">
	<ul>
		<li>
			<a href="/signup">Sign up</a>
		</li>
		<li>
			<a href="/forgot-password">Find a password</a>
		</li>
	</ul>
</div>

<style lang="scss">
	.admin-content {
		font-weight: 500;

		h2 {
			font-size: 26px;
			line-height: 36px;

			&.admin {
				font-size: 20px;
				line-height: 30px;
			}
		}

		p {
			font-size: 16px;
			line-height: 24px;

			&.admin {
				font-size: 12px;
				line-height: 18px;
			}
		}
	}

	/** 로그인 CSS */
	.form-input {
		.input-wrap {
			margin-bottom: 16px;
		}

		.btn-wrap {
			margin-top: 24px;
		}
	}

	.bottom-frame ul {
		display: flex;
		gap: 16px;
		justify-content: space-between;

		li {
			flex: 1;
			color: var(--blue-color);
			font-size: 14px;
			line-height: 20px;
			padding: 6px 0;
		}
	}
</style>
