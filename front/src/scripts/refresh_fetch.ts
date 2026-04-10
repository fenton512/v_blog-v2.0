import { useUserStore } from "@/stores/userStore"
import { HTTPErrType } from "@/types"

export async function refreshFetch(url: string, options: RequestInit):Promise<Response> {
    const userStore = useUserStore()
    options.headers = {
        ...options.headers,
        "Authorization": `Bearer ${userStore.accessToken}`
    }
    let response = await fetch(url, options)
    if (response.status === 401 && response.headers.get("App-Error-Code") === "TOKEN EXPIRED") {
        
        if (await userStore.refresh()) {
            options.headers = {
                ...options.headers,
                "Authorization": `Bearer ${userStore.accessToken}`
            }
            response = await fetch(url, options)
        }
    } 
    if (!response.ok) {
        const error = await response.json()
        console.error(`in fetch response: ${error}`)
        throw {
            detail: error.detail || "Что-то пошло не так" as string,
            status: response.status as number
        }
    }

    return response
}