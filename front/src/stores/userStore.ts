import { defineStore } from "pinia";
import { TokenType, HTTPErrType} from "@/types";
import { refreshFetch } from "@/scripts/refresh_fetch";


export const useUserStore = defineStore("UserStore", {
    state: () => ({
        currentUser: null,
        refreshToken: "",
        accessToken: "",
        _is_refreshing: null as Promise<boolean> | null
    }),
    actions: {
        async refresh(): Promise<boolean> {
            if (this._is_refreshing) {
                return this._is_refreshing 
            }
            const address = process.env.VUE_APP_ROOT_ADDRESS
            this._is_refreshing = ( async () => {
                try {
                    const response = await fetch(`${address}/users/refresh`, {
                        method: "POST",
                        credentials: 'include',
                        // body: JSON.stringify({refresh_token: `${this.refreshToken}`})
                    })
                    if (!response.ok) {
                        const error = await response.json() as HTTPErrType
                        if (error.status == 401 || error.status == 422) { 
                            alert(error.detail)
                            this.logout()
                            return false
                        }
                    }
                    const result = await response.json() as TokenType
                    // this.refreshToken = result.refresh_token
                    this.accessToken = result.access_token
                    return true
                }
                catch (e) {
                    console.error(e)
                    return false
                }
                finally {
                    this._is_refreshing = null
                }
           })();
           return this._is_refreshing
        },
        logout:  () => {
            (this as any).currentUser = null,
            (this as any).refreshToken = "",
            (this as any).accessToken = ""
        },
        async getCurrentUser(): Promise<void>{
            if (!(this as any).accessToken) return
            const address = process.env.VUE_APP_ROOT_ADDRESS
            try {
                const response = await refreshFetch(`${address}/users/me`, {
                    method: "GET",
                    headers: {
                        "Content-Type": 'application/json'
                    }
                })

                this.currentUser = await response.json()
            } catch (e) {
                const err = e as HTTPErrType
                console.log(err)
                alert(err.detail)
            }
        }
    }
})