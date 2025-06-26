<script>
	import { onMount } from 'svelte';
	import { auth } from '../../../../../stores/auth.js';
	import { AlreadyRegisteredAlert } from '$lib/components/modal/index.js';
	import { goto } from '$app/navigation';
	import SignupCompleteAlert from '$lib/components/modal/SignupCompleteAlert.svelte';

	export let data;

	let isSignupCompleteModalOpen = false;
	let isAlreadyRegisteredModalOpen = false;

	onMount(async () => {
		const { email, name, id } = data.data;

		const singupData = {
			email,
			name,
			password1: id,
			password2: id
		};

		const isSignup = await auth.signup(singupData);

		if (isSignup) {
			isSignupCompleteModalOpen = true;
		} else {
			isAlreadyRegisteredModalOpen = true;
		}
	});

	const closeModal = () => {
		isSignupCompleteModalOpen = false;
		isAlreadyRegisteredModalOpen = false;
		goto('/signin');
	};
</script>

<p>Loading...</p>

<SignupCompleteAlert isModalOpen={isSignupCompleteModalOpen} {closeModal} />
<AlreadyRegisteredAlert isModalOpen={isAlreadyRegisteredModalOpen} {closeModal} />
