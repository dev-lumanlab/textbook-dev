export function isValidEmail(email_address) {
	const email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;

	return email_regex.test(email_address);
}
