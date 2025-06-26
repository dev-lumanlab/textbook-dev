<script>
	import { SigninForm } from '$lib/components/auth';
	import { auth } from '../../../stores/auth';
	import { goto } from '$app/navigation';
	import { LoginFailedAlert } from '$lib/components/modal';

	let email = '';
	let password = '';
	let isModalOpen = false;

	const closeModal = () => {
		isModalOpen = false;
	};

	const onSubmit = async () => {
		if (email === '' || password === '') {
			isModalOpen = true;
			return;
		}

		const submitData = { email, password };

		const isLogin = await auth.login(submitData);

		if (isLogin !== true) {
			isModalOpen = true;
		} else {
			goto('/');
		}
	};
</script>

<svelte:head>
	<title>Signin - IACAPAP</title>
</svelte:head>

<SigninForm
	isSignup={false}
	title="IACAPAP Textbook of"
	info="Chil and Adolescent Mental Health ver2.0"
	bind:email
	bind:password
	{onSubmit}
/>
<LoginFailedAlert {isModalOpen} {closeModal} lang="en" />
