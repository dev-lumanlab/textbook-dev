<script>
	import { onMount } from 'svelte';
	import { auth } from '../../../../../stores/auth.js';
	import { NotGoogleOAuthAlert, UnregisteredEmailAlert } from '$lib/components/modal/index.js';
	import { goto } from '$app/navigation';

	export let data;

	let isUnregisteredEmailModalOpen = false;
	let isNotGoogleOAuthModalOpen = false;

	onMount(async () => {
		const { email, name, id } = data.data;

		const signinData = {
			email,
			password: id
		};
		const isLogin = await auth.login(signinData);

		if (isLogin === true) {
			goto('/');
		} else if (isLogin === 401) {
			isNotGoogleOAuthModalOpen = true;
		} else if (isLogin === 404) {
			isUnregisteredEmailModalOpen = true;
		}
	});

	const closeUnregisteredEmailModalOpenModal = () => {
		isUnregisteredEmailModalOpen = false;
		goto('/signup');
	};
	const closeNotGoogleOAuthModalOpenOpenModal = () => {
		isNotGoogleOAuthModalOpen = false;
		goto('/signin');
	};
</script>

<p>Loading...</p>
<UnregisteredEmailAlert
	isModalOpen={isUnregisteredEmailModalOpen}
	closeModal={closeUnregisteredEmailModalOpenModal}
/>
<NotGoogleOAuthAlert
	isModalOpen={isNotGoogleOAuthModalOpen}
	closeModal={closeNotGoogleOAuthModalOpenOpenModal}
/>
