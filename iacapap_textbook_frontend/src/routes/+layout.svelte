<script>
	import 'reset-css';
	import '../styles/main.scss';
	import '../styles/reset.scss';
	import '../styles/common.scss';
	import { page } from '$app/stores';
	import { auth } from '../stores/auth';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	import { browser } from '$app/environment';

	let isLender = false;

	// ID에 '(account)'를 포함하는지 확인하는 함수
	const isAccountRoute = (route) => {
		const idPattern = /\(account\)/;
		return idPattern.test(route.id);
	};

	onMount(async () => {
		if (localStorage.getItem('access_token')) {
			await auth.getUser();
		}
		isLender = true;
	});

	$: {
		if (isLender) {
			const isAuth = $auth.isAuth;
			const level = $auth.level;
			const pathname = $page.url.pathname;

			// 사용자 페이지로의 액세스 권한 확인
			const isUserAccess = isAccountRoute($page.route);

			// 관리자 페이지로의 액세스 권한 확인
			const isAdminAccess = pathname.startsWith('/admin');

			// 사용자가 로그인되지 않은 경우 로그인 페이지로 리디렉션
			if (!isAuth && !isUserAccess && !isAdminAccess) {
				if (!pathname.startsWith('/api')) {
					goto('/signin');
				}
			}

			// 관리자 페이지로의 액세스 권한이 없는 경우 관리자 로그인 페이지로 리디렉션
			if (isAdminAccess && pathname !== '/admin/signin') {
				if (!pathname.startsWith('/api')) {
					if (!isAuth) {
						goto('/admin/signin');
					} else {
						if (level !== 1 && level !== 2) {
							alert('관리자 권한이 없습니다.');
							goto('/');
						}

						if (pathname === '/admin/members') {
							if (level !== 2) {
								alert('마스터 권한이 없습니다.');
								goto('/');
							}
						}
					}
				}
			}
		}
	}

	// if (browser) {
	// 	if (browser) {
	// 		window.addEventListener('unload', function (event) {
	// 			// 페이지가 언로드될 때 실행될 코드 작성
	// 			// 예를 들어, 로그아웃 처리 및 로컬 스토리지의 값 삭제 등을 수행할 수 있습니다.
	// 			if (performance.navigation.type === 1) {
	// 				// 페이지 이탈 시 로그아웃 처리
	// 				auth.logout();
	// 				// 로그아웃 처리 코드를 여기에 작성하세요.
	// 				console.log('logout');
	// 			}
	// 			console.log('unload');
	// 		});
	// 	}
	// }
</script>

<svelte:head>
	<title>IACAPAP</title>
</svelte:head>

<slot />
