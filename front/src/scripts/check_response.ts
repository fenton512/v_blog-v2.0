export async function check_response(url: string, options: RequestInit) {
       const response = await fetch(url, options)
        if (!response.ok) {
           const error = await response.json()
           throw {
               detail: error.detail || "Что-то пошло не так" as string,
               status: response.status as number
           }
       }
       return response 
}