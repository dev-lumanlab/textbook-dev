<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { auth } from '../../stores/auth';
	import LogoutCompleteAlert from './modal/LogoutCompleteAlert.svelte';

	export let menuOpen = false;
	let logoutModalOpen = false;

	const openLogoutModal = () => {
		logoutModalOpen = true;
	};

	const closeLogoutModal = () => {
		logoutModalOpen = false;
	};

	const closeMenu = () => {
		menuOpen = false;
	};

	const handleOutsideClick = (event) => {
		if (!event.target.closest('.menu-container') && !event.target.closest('.menu-open')) {
			closeMenu();
		}
	};

	onMount(() => {
		document.addEventListener('click', handleOutsideClick);
		return () => {
			document.removeEventListener('click', handleOutsideClick);
		};
	});

	const onPasswordUpdate = () => {
		closeMenu();
		goto('/update-password');
	};

	const onLogout = () => {
		closeMenu();
		auth.logout();
		closeLogoutModal();
	};
</script>

{#if menuOpen}
	<div class="menu-container" class:menu-open={menuOpen}>
		<div class="dropdown-menu">
			<button on:click={onPasswordUpdate}>Update password</button>
			<button on:click={openLogoutModal}>Log out</button>
		</div>
	</div>
{/if}

<LogoutCompleteAlert
	isModalOpen={logoutModalOpen}
	closeModal={closeLogoutModal}
	onLogoutDone={onLogout}
/>

<style lang="scss">
	.menu-container {
		display: none;
		position: absolute;
		background-color: #fff;
		z-index: 10;
		top: calc(100% + 10px);
		left: 4px;

		@media (max-width: 1500px) {
			left: inherit;
			right: 4px;
		}

		padding: 3px 0;
		width: 260px;
		border-radius: 6px;
		box-shadow: 0px 10px 15px -3px #00000014;
		box-shadow: 0px 4px 6px -2px #00000005;
		border: 1px solid #eceef0;

		&.menu-open {
			display: block;
		}
	}

	.dropdown-menu {
		button {
			color: var(--text-color);
			width: 100%;
			text-align: left;
			padding: 12px 16px;
			display: block;
			font-size: 16px;
			line-height: 24px;
		}
	}
</style>
