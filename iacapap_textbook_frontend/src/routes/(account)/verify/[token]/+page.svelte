<script>
	import { onMount } from 'svelte';
	import { EmailInput, PasswordInput } from '$lib/components/input';
	import { GoogleSignInDividerGroup } from '$lib/components/auth';
	import {
		isValidPassword,
		validatePasswordError,
		validatePasswordCheckError
	} from '$lib/utils/passwordValidator';
	import ErrorMessage from '$lib/components/ErrorMessage.svelte';
	import { ChangePasswordCompleteAlert, SignupCompleteAlert } from '$lib/components/modal';
	import { goto } from '$app/navigation';
	import { patchChangePassword, postSignup } from '$lib/api/auth';

	/**
	 * @typedef {Object} Data
	 * @property {string} email - The email address.
	 * @property {'signup' | 'password-change'} type - The type of the action, either 'signup' or 'password-change'.
	 */
	/** @type {Data} */
	export let data;

	let isModalOpen = false;

	/**
	 * @typedef {('signup' | 'password-change')} UserActionType
	 * @type {UserActionType}
	 */
	let type = 'signup';

	let email = '';
	let password = '';
	let passwordCheck = '';

	let passwordError = '';
	let passwordCheckError = '';

	let disabled = true;

	onMount(async () => {
		email = data.email;
		type = data.type;
	});

	const closeModal = () => {
		isModalOpen = false;
		goto('/signin');
	};

	$: {
		disabled = !(isValidPassword(password) && password === passwordCheck);
	}

	// 비밀번호 유효성 에러 메시지
	$: {
		passwordError = validatePasswordError(password);
	}

	// 비밀번호 확인 유효성 에러 메시지
	$: {
		passwordCheckError = validatePasswordCheckError(password, passwordCheck);
	}

	const onSubmit = async () => {
		if (passwordError || passwordCheckError) {
			return;
		}

		try {
			if (type === 'signup') {
				const data = {
					email,
					password1: password,
					password2: passwordCheck
				};
				await postSignup(data);
			} else {
				const data = {
					email,
					new_password1: password,
					new_password2: passwordCheck
				};
				await patchChangePassword(data);
			}
			isModalOpen = true;
		} catch (error) {
			console.error(error);
		}
	};
</script>

{#if type === 'signup'}
	<h2>Sign up</h2>
{:else}
	<h2>Please enter a new<br />password.</h2>
{/if}
<form on:submit|preventDefault={onSubmit}>
	<div class="input-wrap">
		<EmailInput label="Enter your email." value={email} disabled={true} />
	</div>
	<div class="input-wrap">
		<PasswordInput
			label={type === 'signup' ? 'Enter your password.' : 'New password'}
			bind:value={password}
		/>
		{#if passwordError}
			<ErrorMessage>{passwordError}</ErrorMessage>
		{/if}
	</div>
	<div class="input-wrap">
		<PasswordInput
			label={type === 'signup' ? 'Check the password.' : 'Check the new password.'}
			bind:value={passwordCheck}
		/>
		{#if passwordCheckError}
			<ErrorMessage>{passwordCheckError}</ErrorMessage>
		{/if}
	</div>
	<div>
		<button class="btn type1" type="submit" class:disabled>
			{type === 'signup' ? 'Create account' : 'Reset password'}
		</button>
	</div>
</form>
<GoogleSignInDividerGroup />

{#if type === 'signup'}
	<SignupCompleteAlert {isModalOpen} {closeModal} />
{:else}
	<ChangePasswordCompleteAlert {isModalOpen} {closeModal} />
{/if}

<style lang="scss">
	h2 {
		font-size: 26px;
		line-height: 36px;
		font-weight: 500;
	}

	.input-wrap {
		margin-bottom: 24px;
	}
</style>
