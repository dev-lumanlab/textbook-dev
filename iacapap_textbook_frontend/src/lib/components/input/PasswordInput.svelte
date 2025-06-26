<script>
	import { EyeOff, Eye } from '$lib/components/icons';
	import { v4 as uuidv4 } from 'uuid';

	export let label;
	export let value = '';
	let type = 'password';

	const inputToggle = () => {
		type = type === 'password' ? 'text' : 'password';
	};

	const id = uuidv4();

	const handleInput = (event) => {
		value = event.target.value;
	};
</script>

<div class="password-toggle">
	<input {type} {value} {id} on:input={handleInput} class="input type1" required />
	<label for={id} class="input-label">{label}</label>
	<button type="button" on:click={inputToggle}>
		{#if type === 'password'}
			<Eye />
		{:else}
			<EyeOff />
		{/if}
	</button>
</div>

<style lang="scss">
	.password-toggle {
		position: relative;

		input:focus {
			border: 1px solid var(--blue-color);
		}

		input {
			padding-right: 50px;
			&:is(:focus, :valid) + .input-label {
				top: -7px;
				padding: 0 4px;
				font-size: 12px;
				line-height: 18px;
				z-index: 10;
				bottom: initial;
			}

			&:valid + .input-label {
				color: var(--slate-base-color);
			}

			&:focus + .input-label {
				color: var(--blue-color);
			}
		}

		.input-label {
			position: absolute;
			top: 18px;
			left: 13px;
			background-color: #fff;
			color: var(--slate-base-color);
			transition: 0.3s;
			cursor: text;
		}

		button {
			position: absolute;
			width: 24px;
			height: 24px;
			right: 16px;
			top: 0;
			bottom: 0;
			margin: auto;
			padding: 2px;
			cursor: pointer;
		}
	}
</style>
