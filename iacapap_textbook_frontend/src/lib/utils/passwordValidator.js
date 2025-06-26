const lengthRegex = /^.{8,}$/;
const specialCharRegex = /[!@#$%^&*?_~]/;

function checkPasswordLength(password) {
	return lengthRegex.test(password);
}

function checkPasswordSpecialChar(password) {
	return specialCharRegex.test(password);
}

export function isValidPassword(password) {
	return lengthRegex.test(password) && specialCharRegex.test(password);
}

export function validatePasswordError(password) {
	const hasValidLength = checkPasswordLength(password);
	const hasSpecialChar = checkPasswordSpecialChar(password);

	if (password.length < 1) return;
	if (hasValidLength && hasSpecialChar) {
		return '';
	} else if (!hasValidLength) {
		return '비밀번호는 8자리 이상이어야 합니다.';
	} else {
		return '다음 특수문자를 포함해야 합니다: (!,@,#,$,%,^,&,*,?,_,~)';
	}
}

export function validatePasswordCheckError(password, passwordCheck) {
	if (passwordCheck.length < 1) return;

	if (password !== passwordCheck) {
		return '입력하신 비밀번호를 확인해 주세요.';
	} else {
		return '';
	}
}
