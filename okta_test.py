"""
Auth0 JWT Validator

Main validator class for validating JWT ID tokens with comprehensive
claim and header validation.
"""

from datetime import datetime
from typing import Optional

from .exceptions.tokens import (
    BadExpirationClaim,
    BadIssuedAtTimeClaim,
    ClaimMissing,
    ClaimMismatch,
    HeaderMissing,
    HeaderMismatch,
)
from .utilities.token import Token


class Validator:
    """
    Validates Auth0 ID tokens ensuring all required claims and headers are present
    and valid according to OIDC specifications.
    """

    def __init__(
            self,
            token: str,
            issuer: str,
            client_id: str,
            nonce: Optional[str] = None,
    ):
        """
        Initialize the validator and perform token validation.

        Args:
            token: JWT token to validate
            issuer: Expected 'iss' claim value
            client_id: Expected audience ('aud') claim value
            nonce: Optional expected 'nonce' claim value
        """
        self.token = token
        self.issuer = issuer
        self.client_id = client_id
        self.nonce = nonce

        # Decode the token
        decoded = Token.decode(token)
        headers = decoded.headers
        claims = decoded.claims
        print(f"claims = {claims.nonce}, nonce = {self.nonce}")

        if (not headers) or ('alg' not in headers.__dict__) or (not headers.alg):
            raise HeaderMissing(header='alg')
        elif headers.alg != 'RS256':
            raise HeaderMismatch(
                header='alg',
                expected='RS256',
                actual=headers.alg)
        # validate ClaimMissing
        if not claims:
            raise ClaimMissing()
        if not claims.iss:
            raise ClaimMissing("iss")
        if not claims.sub:
            raise ClaimMissing("sub")
        if not claims.iat:
            raise ClaimMissing("iat")
        if not claims.exp:
            raise ClaimMissing("exp")
        if not claims.aud:
            raise ClaimMissing("aud")

            # validate ClaimMismatch
        if claims.iss != self.issuer:
            raise ClaimMismatch(claim='iss',
                                expected=self.issuer,
                                actual=claims.iss)
        if claims.iat > datetime.now():
            raise BadIssuedAtTimeClaim()
        if claims.exp < datetime.now():
            raise BadExpirationClaim()
        if type(claims.aud) is str:
            if not claims.aud == self.client_id:
                raise ClaimMismatch(
                    claim='aud',
                    expected=self.client_id, actual=claims.aud)
        elif type(claims.aud) is list:
            if self.client_id not in claims.aud:
                raise ClaimMismatch(
                    claim='aud',
                    expected=self.client_id,
                    actual=', '.join(claims.aud))

        # if claims.nonce:
        #     if self.nonce:
        #         if claims.nonce != self.nonce:
        #             raise ClaimMismatch(
        #                 claim='nonce',
        #                 expected=self.nonce,
        #                 actual=claims.nonce)
        # if claims.nonce != self.nonce:
        #       raise ClaimMismatch(
        #                 claim='nonce',
        #                 expected=self.nonce,
        #                 actual=claims.nonce)
        if claims.nonce:
            if self.nonce:
                if claims.nonce != self.nonce:
                    raise ClaimMismatch(
                        claim='nonce',
                        expected=self.nonce,
                        actual=claims.nonce)
        # if self.nonce:
        #     if claims.nonce :
        #         raise ClaimMismatch(
        #                 claim='nonce',
        #                 expected=self.nonce,
        #                 actual=claims.nonce)
