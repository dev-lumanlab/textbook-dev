<script>
	import { v4 as uuidv4 } from 'uuid';

	export let label;
	export let value = '';
	export let disabled = false;

	const id = uuidv4();
</script>

<div class="input-toggle">
	<input type="text" bind:value {id} class="input type1" required {disabled} />
	<label for={id} class="input-label">{label}</label>
</div>

<style lang="scss">
	.input-toggle {
		position: relative;

		input {
			&:is(:focus, :valid, :disabled) + .input-label {
				top: -7px;
				padding: 0 4px;
				font-size: 12px;
				line-height: 18px;
				z-index: 10;
				bottom: initial;
			}

			&:disabled {
				// color:
				color: rgba(17, 24, 28, 0.5);
				// opacity: 0.5;
			}

			&:disabled + .input-label {
				background: linear-gradient(to bottom, #fff 35%, #f8f9fa 45%);
				// background: #f8f9fa;
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

		input:focus {
			border: 1px solid var(--blue-color);
		}
	}
</style>
