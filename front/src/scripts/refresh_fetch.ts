import { useUserStore } from "@/stores/userStore"
import { HTTPErrType } from "@/types"

//need additional logic for checking userStore.accessToken
export async function refreshFetch(url: string, options: RequestInit):Promise<Response> {
    const unexpectedErr = {
                detail: "Произошла непредвиденная ошибка, пожалуйста войдите в аккаунт еще раз",
                status: 401
            }
    const refreshToken = async() => {
        if (await userStore.refresh()) {
            options.headers = {
                ...options.headers,
                "Authorization": `Bearer ${userStore.accessToken}`
            }
            return true
        }
        return false
    }
    const userStore = useUserStore()
    if (!userStore.accessToken) {
        if (await refreshToken()) {
            return refreshFetch(url, options)
        } else {
            throw {
               unexpectedErr
            }
        }
    }
    options.headers = {
        ...options.headers,
        "Authorization": `Bearer ${userStore.accessToken}`
    }
    let response = await fetch(url, options)
    if (response.status === 401 && response.headers.get("App-Error-Code") === "TOKEN EXPIRED") {
        
        if (await refreshToken()) {
            response = await fetch(url, options)
        } else {
            throw unexpectedErr
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