'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import Image from 'next/image'
import { useRouter } from 'next/navigation'
import axios from 'axios'

import { Button } from '@/components/ui/button'

const loginSchema = z.object({
  email: z
    .string()
    .min(1, { message: 'メールアドレスを入力してください。' })
    .email({ message: '無効なメールアドレスです。' }),
  password: z
    .string()
    .min(1, { message: 'パスワードを入力してください。' })
    .min(8, { message: 'パスワードは８文字以上である必要があります。' }),
})

interface IFormInput {
  email: string
  password: string
}

function LoginPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<IFormInput>({
    resolver: zodResolver(loginSchema),
  })
  const router = useRouter()

  const onSubmit = async (data: IFormInput) => {
    console.log(data)
    const email = data.email
    const password = data.password

    // TODO: post url
    axios
      .post('http://localhost:8080/login', { email, password })
      .then((response) => {
        localStorage.setItem('token', response.data.token)
        router.push('/top')
      })
      .catch((error) => {
        console.error('ログインに失敗しました', error)
      })
  }

  return (
    <>
      <Image
        alt="login back ground image"
        src={`/login.webp`}
        quality={100}
        fill
        sizes="100vw"
        objectFit={`cover`}
        className="z-0"
      />
      <div className="z-1 absolute flex items-center gap-2 rounded p-2 backdrop-blur-sm">
        <Image
          alt="logo"
          src={`/logo.png`}
          quality={50}
          width={50}
          height={100}
          className="rounded bg-white/50"
        />
        <p className="font-serif text-2xl font-bold text-white">
          Winnings Whisper
        </p>
      </div>
      <div className="flex h-screen items-center justify-center">
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="z-10 mt-[-25px] space-y-6 rounded-2xl bg-black/50 p-12 backdrop-blur-sm"
        >
          <div className="text-center text-4xl font-black text-white">
            <p>Login</p>
          </div>
          <div>
            <label htmlFor="email" className="text-sm font-bold text-white">
              Email
            </label>
            <input
              type="email"
              defaultValue="demo@demo.co.jp"
              {...register('email')}
              className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500"
            />
            {errors.email && (
              <p className="mt-2 text-sm text-red-600">
                {errors.email.message}
              </p>
            )}
          </div>
          <div>
            <label htmlFor="password" className="text-sm font-bold text-white">
              Password
            </label>
            <input
              type="password"
              defaultValue="password"
              {...register('password')}
              className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500"
            />
            {errors.password && (
              <p className="mt-2 text-sm text-red-600">
                {errors.password.message}
              </p>
            )}
          </div>
          <div>
            <Button type="submit" className="w-full" variant="default">
              Log in
            </Button>
          </div>
        </form>
      </div>
    </>
  )
}

export default LoginPage
