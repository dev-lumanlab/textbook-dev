<script>
	import { getUser, postSendEmail } from '$lib/api/auth';
	import Loading from '$lib/components/Loading.svelte';
	import { ForgotPasswordStep1, SignupStep2 } from '$lib/components/auth';
	import { UnregisteredEmailAlert } from '$lib/components/modal';

	let isModalOpen = false;
	let isLoading = false;
	let step = 1;
	let email = '';

	const closeModal = () => {
		isModalOpen = false;
	};

	const onSubmit = async () => {
		if (step === 1) {
			try {
				await getUser(email);
				isLoading = true;
				const response = await postSendEmail(email, 'password-change');
				if (response.ok) {
					isLoading = false;
					step = 2;
				}
			} catch (e) {
				console.error(e);
				isModalOpen = true;
			}
		}
	};
</script>

<svelte:head>
	<title>Forgot Password - IACAPAP</title>
</svelte:head>

{#if step === 1}
	<ForgotPasswordStep1 bind:email {onSubmit} />
{:else}
	<SignupStep2 {email} {onSubmit} />
{/if}

<Loading isOpen={isLoading} />

<UnregisteredEmailAlert {isModalOpen} {closeModal} />
