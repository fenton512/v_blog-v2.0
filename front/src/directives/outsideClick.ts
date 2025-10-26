import { DirectiveBinding, type Directive } from "vue";


declare global {
    //tell ts that HTMLElement has a property _out...
    interface HTMLElement {
        _outsideClickHandler?: (event: Event) => void
    }
}

export const clickOutside: Directive =  {
    //befor element will be rendered
    beforeMount: (
        //we pass element itself and custom handler
        el: HTMLElement, 
        binding: DirectiveBinding<(event: Event)  => void>
     ) => {
        el._outsideClickHandler = (event: Event) => {
            if (event.target !== el && !el.contains(event.target as Node)){
                if (typeof(binding.value) === 'function') {
                    binding.value(event)
                }
            }
        }
        document.addEventListener('click', el._outsideClickHandler)
    },
    unmounted(el: HTMLElement) {
        if (el._outsideClickHandler) {
            document.removeEventListener('click', el._outsideClickHandler)
        }
    }
}