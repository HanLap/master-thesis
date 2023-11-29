import { mount } from 'svelte';
import App from './App.svelte'
import config from './config';

// @ts-ignore
const app = mount(App, {
  target: document.getElementById('app'),
  props: config
})

export default app
