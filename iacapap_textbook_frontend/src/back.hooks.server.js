// import { auth } from './stores/auth';
// import { redirect } from '@sveltejs/kit';
// import { get } from 'svelte/store';

// // ID에 '(account)'를 포함하는지 확인하는 함수
// const isAccountRoute = (route) => {
// 	const idPattern = /\(account\)/;
// 	return idPattern.test(route.id);
// };

// export const handle = async ({ event, resolve }) => {
// 	const isRefresh = event.request.headers.get('sec-fetch-mode') === 'navigate';

// 	if (isRefresh) {
// 		// 새로고침 시 수행할 로직
// 		// console.log('새로고침');
// 		const cookieHeader = event.request.headers.get('Cookie');
// 		// console.log(cookieHeader, 'asdf');
// 	}

// 	const { isAuth, role } = get(auth);
// 	const { pathname } = event.url;

// 	// 사용자 페이지로의 액세스 권한 확인
// 	const isUserAccess = isAccountRoute(event.route);
// 	// 관리자 페이지로의 액세스 권한 확인
// 	// const isAdminAccess = pathname.startsWith('/admin') && role !== 'admin';
// 	const isAdminAccess = pathname.startsWith('/admin') && !isAuth;

// 	// 사용자가 로그인되지 않은 경우 로그인 페이지로 리디렉션
// 	if (!isAuth && !isUserAccess && !isAdminAccess) {
// 		if (!pathname.startsWith('/api')) {
// 			throw redirect(303, '/signin');
// 		}
// 	}

// 	// 관리자 페이지로의 액세스 권한이 없는 경우 관리자 로그인 페이지로 리디렉션
// 	if (isAdminAccess && pathname !== '/admin/signin') {
// 		if (!pathname.startsWith('/api')) {
// 			throw redirect(303, '/admin/signin');
// 		}
// 	}

// 	const response = await resolve(event);
// 	return response;
// };
