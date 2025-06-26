<script>
	import { goto } from '$app/navigation';
	import { SigninForm } from '$lib/components/auth';
	import { LoginFailedAlert } from '$lib/components/modal';
	import { auth } from '../../../../stores/auth';

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
			goto('/admin');
		}
	};
</script>

<svelte:head>
	<title>Admin Signin - IACAPAP</title>
</svelte:head>

<SigninForm
	role="admin"
	title="ADMIN"
	info="IACAPAP Textbook of Chil and Adolescent Mental Health ver2.0"
	bind:email
	bind:password
	{onSubmit}
/>
<LoginFailedAlert {isModalOpen} {closeModal} lang="ko" />
