from blspy import (
    G1Element as G1,
    G2Element as G2,
    BasicScheme as BSc,
    AugScheme as ASc,
    PopScheme as PSc,
    PrivateKey,
    _Core as Core
)

from py_ecc.bls import (
    G2Basic,
    G2MessageAugmentation as G2MA,
    G2ProofOfPossession as G2Pop
)
from py_ecc.fields import (
    optimized_bls12_381_FQ as FQ,
    optimized_bls12_381_FQ2 as FQ2,
    optimized_bls12_381_FQ12 as FQ12,
    optimized_bls12_381_FQP as FQP,
)
# X = FQ2([0x0a650bd36ae7455cb3fe5d8bb1310594551456f5c6593aec9ee0c03d2f6cb693bd2c5e99d4e23cbaec767609314f51d3, 0x0fbdae26f9f9586a46d4b0b70390d09064ef2afe5c99348438a3c7d9756471e015cb534204c1b6824617a85024c772dc])
# Y = FQ2([0x0d8d49e7737d8f9fc5cef7c4b8817633103faf2613016cb86a1f3fc29968fe2413e232d9208d2d74a89bf7a48ac36f83, 0x02e5cf8f9b7348428cc9e66b9a9b36fe45ba0b0a146290c3a68d92895b1af0e1f2d9f889fb412670ae8478d8abd4c5aa])
        # (b'abc',
        # FQ2([0x1953ce6d4267939c7360756d9cca8eb34aac4633ef35369a7dc249445069888e7d1b3f9d2e75fbd468fbcbba7110ea02, 0x03578447618463deb106b60e609c6f7cc446dc6035f84a72801ba17c94cd800583b493b948eff0033f09086fdd7f6175]),
        # FQ2([0x0882ab045b8fe4d7d557ebb59a63a35ac9f3d312581b509af0f8eaa2960cbc5e1e36bb969b6e22980b5cbdd0787fcf4e, 0x0184d26779ae9d4670aca9b267dbd4d3b30443ad05b8546d36a195686e1ccc3a59194aea05ed5bce7c3144a29ec047c4])),
        

secret = 3
pk = G2Basic.SkToPk(secret)
sig = G2Basic.Sign(secret, b'')
print(pk.hex())
print(sig.hex())

pk = G2Basic.SkToPk(secret)
sig = G2Basic.Sign(secret, bytes([1,2,3]))
print(pk.hex())
print("SEG HEX")
print(sig.hex())
"""
msg b''
DST b'BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_NUL_'
u0 (2096646833598254574567476328917767060610770959819732383916597724864026655033824166836700488978229614793838161354202, 6998399729131158633900098615751478410389520769362086648745096077525896192415232576726852480396711664051994852485)
u1 (286758494997223394558042312553677761300464196897885340676151095316452509505708828522397663205328365272415050990717, 1642418930882865242848684086464074867103706919465608576146376481470167375213264283016947092633683307128828514765367)
q0a 0x937ac22efb5b97ce5a9e820c29cda00f8883651cae7890eb82dcd156456bd17bf2b6e940b0c616abbe28d3713eda9634
q0b 0x137bf36fb69ac0a0845c03a685d3522f61f9929e8fc50efbd8ad4a0c9a963cbebce3f709ad7debd0329df33fd16d74f7
q1a 0x8524034d87e39688d47bf9639e43d7908ab8b086015bcf03dc515af0891eb0418af42b8b8b731fbf30e7d74844853ccd
q1b 0x18572b878b1c15f46967273a6e8d0bfb6b3e8628441c937cf245d57731e3aa186b53f48a7e2c6814b58d3d9d2248cdf7
r ((1426061248016476521034631754978531023073132919759423981082993578169425562586298534512432393505927573380244953338496, 15179048928141926547300286373237806517751883881783206498326862982368684870346318744534146799974494727645833487420), (3349663469334620722023009498726489891687700838521138152201541770015608230486959422229194765940827968319319851398503, 3582688379600200433203882578910578037639630508257663483588036588885911456300877277378302999895811732179204738384055), (2277127526838458794895595377478167569601623718400170164031042926163668924389021751724453089344995911298483447116805, 1470710632001767112788486860823645705921249396580170155750698215540603582275592831804180351643824766802161090685479))
p ((1123832777638759527020815348945496689714453957741102233246328596560536109645240791242387186444484449734061892268596, 936374954762637757776230380425043974449036252147106787408445676719152497915975096477695445406052279790925585667477), (2509184947550584807300805078821386830277106158925287861072700764961774629003719482055472807693516547010046183556288, 270157279123393611879514207907401850998515555672973531009278637505806837541305029531056137070598747096624850508290), (3210922848251195291203125886824830919794027816754843169288267532200095922088203106396296131750306111684034044516654, 1777276810214439066192644614199903187891356179799905518562656423385530802157684393230352209872697841506018952206386))



89ece308f9d1f0131765212deca99697b112d61f9be9a5f1f3780a51335b3ff981747a0b2ca2179b96d2c0c9024e5224
a9c204063d3fd088bc16a929e88e10cac14f6888f5d14002fda672afafc660f7006a92f6e79df093af68e8b239983cb7
092deda9417379772c34a4bced911147ff5ce823c230cea8bc2785f3db55185703e40f1d2095642948cc4524fe7ab5d8
89ece308f9d1f0131765212deca99697b112d61f9be9a5f1f3780a51335b3ff981747a0b2ca2179b96d2c0c9024e5224
9669f552439cbc2a67b33a512c2b59c5da7fc3fdee27f558744e27e2aaa79536e0c74ef6f936bc61a385ea016810954416a1609ea4f4832b2f2fa56ac77286fca8099fe0ace7c22f3be897bd04ecd2863eb04237a5978de9250c86bf1a5648ba

NEWEST:
a3ddbea75598f517e5de7d259345d60b2311cac8e83f945c0445179ed3bf1bdadc66f3632eed2db3492f350c9889a80a0b4b9e9c842fabb57c7f999dbe56ced37be2f797563b86f9dbf1a3843c03afb30a3e829255c6b6a09647c3d115aea1f0


SIG1: 0b4b9e9c842fabb57c7f999dbe56ced37be2f797563b86f9dbf1a3843c03afb30a3e829255c6b6a09647c3d115aea1f003ddbea75598f517e5de7d259345d60b2311cac8e83f945c0445179ed3bf1bdadc66f3632eed2db3492f350c9889a80a
g2pt is: 15c01566993d4469805df3e1f29b536481a832bf2751b6908faed6776d062d585521889232999d72b679d6e38bb5cfff08aab303e33ed14f4a904004a92bd26ffc969c1d1e7d4b7f0c04150a73e1845a911e51a2b2d369d5cef06560c5ac9f57
SIG0: 
892deda9417379772c34a4bced911147ff5ce823c230cea8bc2785f3db55185703e40f1d2095642948cc4524fe7ab5d8
09c204063d3fd088bc16a929e88e10cac14f6888f5d14002fda672afafc660f7006a92f6e79df093af68e8b239983cb7

"""

"""
msg = []
msg_bytes = bytes(msg)

for secret in range(3,4):
    for k in range(1):
        secret_bytes = bytes([0] * 31 + [secret])
        sk = PrivateKey.from_bytes(secret_bytes)
        # pk1a = BSc.sk_to_g1(sk)
        # pk1b = ASc.sk_to_g1(sk)
        # pk1c = PSc.sk_to_g1(sk)
        sig1a = BSc.sign(sk, [])
        # sig1b = ASc.sign(sk, [0] * 29 + msg)
        # sig1c = PSc.sign(sk, [0] * 29 + msg)

        print('-')#blspy')
        #print(sk)
        # print(pk1a)
        # print(pk1b)
        # print(pk1c)

        s = str(sig1a)
        print(s)
        # print(sig1b)
        # print(sig1c)

        # pk2a = G2Basic.SkToPk(secret)
        # pk2b = G2MA.SkToPk(secret)
        # pk2c = G2Pop.SkToPk(secret)
        sig2a = G2Basic.Sign(secret, msg_bytes)
        # sig2b = G2MA.Sign(secret, msg_bytes)
        # sig2c = G2Pop.Sign(secret, msg_bytes)
        #print('pyecc')
        # print(pk2a.hex())
        # print(pk2b.hex())
        # print(pk2c.hex())
        
        print(sig2a.hex())
        # print(sig2b.hex())
        # print(sig2c.hex())
"""

import random

for trials in range(0):
    secret = 1 << 500 #random.randint(0, 123456789)
    """
    lst = [0] * 32
    x = secret
    for i in range(31, -1, -1):
        lst[i] = x % 256
        x //= 256
    secret_bytes = bytes(lst)
    sk = PrivateKey.from_bytes(secret_bytes)
    pk = BSc.sk_to_g1(sk)
    sig = BSc.sign(sk, msg)

    #print('blspy')
    #print(sk)
    #print(pk)
    #print(sig)
    """
    pk2 = G2Basic.SkToPk(secret)
    sig2 = G2Basic.Sign(secret, msg_bytes)
    #print('pyecc')
    #print(pk2.hex())
    #print(sig2.hex())
    lhs = str(pk)
    rhs = pk2.hex()
    print('LHS', lhs)
    print('RHS', rhs)

"""
if 0:
    import pytest
    from py_ecc.bls import G2Basic

    @pytest.mark.parametrize(
        'SKs,messages,success',
        [
            (range(10), range(10), True),
            (range(3), (b'42', b'69', b'42'), False),  # Test duplicate messages fail
        ]
    )
    def test_aggregate_verify(SKs, messages, success):
        PKs = [G2Basic.SkToPk(SK) for SK in SKs]
        messages = [bytes(msg) for msg in messages]
        signatures = [G2Basic.Sign(SK, msg) for SK, msg in zip(SKs, messages)]
        aggregate_signature = G2Basic.Aggregate(signatures)
        assert G2Basic.AggregateVerify(PKs, messages, aggregate_signature) == success
"""