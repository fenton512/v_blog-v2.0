export interface PostType {
    id: number,
    text: string,
    author: AuthorType
    created_at: Date,
    updated_at: Date,
    comments: CommentType[]

    
}

export interface CurrentUserType {
    id: number,
    email: string,
    nickname: string,
    role: string,
    avatat_url: string,
    description: string
}

export interface AuthorType {
    nickname: string,
    id: number,
    avatar_url: string
}

export interface TokenType {
    refresh_token: string,
    access_token: string,
    token_type: string
}

export interface CommentType {
    text: string,
    id: number,
    author: AuthorType,
    created_at: Date,
    updated_at: Date
}


export interface HTTPErrType {
    detail: string,
    status: number
}