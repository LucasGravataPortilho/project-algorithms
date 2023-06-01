def find_duplicate(nums):
    if nums is None or len(nums) <= 1:
        return False

    numeros_iguais = set()

    for numero in nums:
        if isinstance(numero, str) or numero < 0:
            return False
        if numero in numeros_iguais:
            return numero
        numeros_iguais.add(numero)

    return False
