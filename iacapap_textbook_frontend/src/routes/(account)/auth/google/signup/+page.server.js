import { PUBLIC_GOOGLE_CLIENT_ID, PUBLIC_GOOGLE_CLIENT_PW } from '$env/static/public';

export const load = async ({ fetch, url }) => {
	const code = url.searchParams.get('code');
	const response = await fetch('https://oauth2.googleapis.com/token', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		body: new URLSearchParams({
			client_id: PUBLIC_GOOGLE_CLIENT_ID,
			client_secret: PUBLIC_GOOGLE_CLIENT_PW,
			redirect_uri: `${url.origin}/auth/google/signup`,
			code: code,
			grant_type: 'authorization_code'
		})
	});

	const { access_token, token_type } = await response.json();

	const userResponse = await fetch('https://www.googleapis.com/userinfo/v2/me', {
		headers: {
			Authorization: `${token_type} ${access_token}`
		}
	});

	const data = await userResponse.json();

	return {
		data
	};
};
