<script>
	import { PasswordInput, EmailInput } from '$lib/components/input';
	import { onMount } from 'svelte';
	import { auth } from '../../../stores/auth';
	import { goto } from '$app/navigation';
	import {
		isValidPassword,
		validatePasswordCheckError,
		validatePasswordError
	} from '$lib/utils/passwordValidator';
	import { ChangePasswordCompleteAlert } from '$lib/components/modal';
	import ErrorMessage from '$lib/components/ErrorMessage.svelte';
	import { patchChangePassword } from '$lib/api/auth';

	let email;

	let password = '';
	let passwordCheck = '';

	let isModalOpen = false;

	$: disabled = !(isValidPassword(password) && password === passwordCheck);
	// 비밀번호 유효성 에러 메시지
	$: passwordError = validatePasswordError(password);
	// 비밀번호 확인 유효성 에러 메시지
	$: passwordCheckError = validatePasswordCheckError(password, passwordCheck);

	onMount(() => {
		email = $auth.email;

		if (!$auth.isAuth) {
			goto('/signin');
		}
	});

	const onSubmit = async () => {
		if (passwordError || passwordCheckError) {
			return;
		}

		try {
			const data = {
				email,
				new_password1: password,
				new_password2: passwordCheck
			};
			await patchChangePassword(data);
			isModalOpen = true;
		} catch (error) {
			console.error(error);
		}
	};

	const closeModal = () => {
		isModalOpen = false;
		goto('/');
	};
</script>

<svelte:head>
	<title>Update Password - IACAPAP</title>
</svelte:head>

<h2>Please enter a new<br /> password.</h2>
<div class="form-input">
	<form on:submit|preventDefault={onSubmit}>
		<div class="input-wrap">
			<EmailInput label="Enter your email" disabled value={email} />
		</div>
		<div class="input-wrap">
			<PasswordInput label="New password." bind:value={password} />
			{#if passwordError}
				<ErrorMessage>{passwordError}</ErrorMessage>
			{/if}
		</div>
		<div class="input-wrap">
			<PasswordInput label="Check the new password." bind:value={passwordCheck} />
			{#if passwordCheckError}
				<ErrorMessage>{passwordCheckError}</ErrorMessage>
			{/if}
		</div>
		<div class="btn-wrap">
			<button class="btn type1" class:disabled {disabled}>Reset password</button>
		</div>
	</form>
</div>

<ChangePasswordCompleteAlert {isModalOpen} {closeModal} />

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
