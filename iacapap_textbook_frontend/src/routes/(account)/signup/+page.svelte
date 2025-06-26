<script>
	import { getUser, postSendEmail } from '$lib/api/auth';
	import Loading from '$lib/components/Loading.svelte';
	import { SignupStep1, SignupStep2 } from '$lib/components/auth';
	import { AlreadyRegisteredAlert } from '$lib/components/modal';

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
				isModalOpen = true;
			} catch (e) {
				console.error(e);
				isLoading = true;
				const response = await postSendEmail(email);
				if (response.ok) {
					isLoading = false;
					step = 2;
				}
			}
		}
	};
</script>

<svelte:head>
	<title>Signup - IACAPAP</title>
</svelte:head>

{#if step === 1}
	<SignupStep1 {onSubmit} bind:email />
{:else if step === 2}
	<SignupStep2 {email} {onSubmit} />
{/if}

<Loading isOpen={isLoading} />

<AlreadyRegisteredAlert {isModalOpen} {closeModal} />
